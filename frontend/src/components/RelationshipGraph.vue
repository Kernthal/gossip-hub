<template>
  <div ref="graphContainer" class="relationship-graph">
    <svg ref="svgRef" class="graph-svg"></svg>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import * as d3 from 'd3'

const props = defineProps({
  data: {
    type: Object,
    default: () => ({ nodes: [], links: [] })
  },
  width: {
    type: Number,
    default: 800
  },
  height: {
    type: Number,
    default: 500
  }
})

const graphContainer = ref(null)
const svgRef = ref(null)
let simulation = null

onMounted(() => {
  initGraph()
})

onUnmounted(() => {
  if (simulation) {
    simulation.stop()
  }
})

watch(() => props.data, () => {
  updateGraph()
}, { deep: true })

function initGraph() {
  const svg = d3.select(svgRef.value)
  svg.attr('width', props.width).attr('height', props.height)

  // Add zoom behavior
  const zoom = d3.zoom()
    .scaleExtent([0.1, 4])
    .on('zoom', (event) => {
      svg.select('g').attr('transform', event.transform)
    })

  svg.call(zoom)

  // Create main group
  svg.append('g')

  // Add arrow markers
  svg.append('defs').append('marker')
    .attr('id', 'arrowhead')
    .attr('viewBox', '-0 -5 10 10')
    .attr('refX', 20)
    .attr('refY', 0)
    .attr('orient', 'auto')
    .attr('markerWidth', 6)
    .attr('markerHeight', 6)
    .append('path')
    .attr('d', 'M 0,-5 L 10,0 L 0,5')
    .attr('fill', '#999')

  updateGraph()
}

function updateGraph() {
  if (!props.data.nodes || props.data.nodes.length === 0) return

  const svg = d3.select(svgRef.value)
  const g = svg.select('g')

  // Clear previous
  g.selectAll('*').remove()

  // Create force simulation
  simulation = d3.forceSimulation(props.data.nodes)
    .force('link', d3.forceLink(props.data.links).id(d => d.id).distance(100))
    .force('charge', d3.forceManyBody().strength(-300))
    .force('center', d3.forceCenter(props.width / 2, props.height / 2))
    .force('collision', d3.forceCollide().radius(30))

  // Draw links
  const link = g.append('g')
    .selectAll('line')
    .data(props.data.links)
    .enter().append('line')
    .attr('stroke', '#999')
    .attr('stroke-opacity', 0.6)
    .attr('stroke-width', d => Math.sqrt(d.weight || 1))
    .attr('marker-end', 'url(#arrowhead)')

  // Draw nodes
  const node = g.append('g')
    .selectAll('g')
    .data(props.data.nodes)
    .enter().append('g')
    .call(d3.drag()
      .on('start', dragstarted)
      .on('drag', dragged)
      .on('end', dragended))

  // Node circles
  node.append('circle')
    .attr('r', d => d.radius || 20)
    .attr('fill', d => d.color || '#667eea')
    .attr('stroke', '#fff')
    .attr('stroke-width', 2)
    .style('cursor', 'pointer')

  // Node labels
  node.append('text')
    .text(d => d.name)
    .attr('text-anchor', 'middle')
    .attr('dy', '.35em')
    .attr('fill', '#fff')
    .attr('font-size', 12)
    .attr('font-weight', 600)
    .style('pointer-events', 'none')

  // Node hover effects
  node.on('mouseenter', function(event, d) {
    d3.select(this).select('circle')
      .transition()
      .duration(200)
      .attr('r', (d.radius || 20) * 1.2)
  }).on('mouseleave', function(event, d) {
    d3.select(this).select('circle')
      .transition()
      .duration(200)
      .attr('r', d.radius || 20)
  })

  // Update positions
  simulation.on('tick', () => {
    link
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y)

    node.attr('transform', d => `translate(${d.x},${d.y})`)
  })
}

function dragstarted(event, d) {
  if (!event.active) simulation.alphaTarget(0.3).restart()
  d.fx = d.x
  d.fy = d.y
}

function dragged(event, d) {
  d.fx = event.x
  d.fy = event.y
}

function dragended(event, d) {
  if (!event.active) simulation.alphaTarget(0)
  d.fx = null
  d.fy = null
}
</script>

<style scoped>
.relationship-graph {
  width: 100%;
  height: 100%;
  min-height: 400px;
}

.graph-svg {
  width: 100%;
  height: 100%;
}
</style>
