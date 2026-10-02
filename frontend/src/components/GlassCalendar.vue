<template>
  <div class="glass-calendar">
    <div class="calendar-header">
      <button class="calendar-nav" @click="prevMonth">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path d="M10 12L6 8L10 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      <span class="calendar-title">{{ currentMonth }}</span>
      <button class="calendar-nav" @click="nextMonth">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path d="M6 4L10 8L6 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
    </div>
    <div class="calendar-grid">
      <div v-for="day in weekDays" :key="day" class="calendar-weekday">
        {{ day }}
      </div>
      <div
        v-for="date in calendarDates"
        :key="date.key"
        class="calendar-date"
        :class="{
          'is-today': date.isToday,
          'is-selected': date.isSelected,
          'is-other-month': !date.isCurrentMonth
        }"
        @click="selectDate(date)"
      >
        {{ date.day }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  modelValue: {
    type: Date,
    default: () => new Date()
  }
})

const emit = defineEmits(['update:modelValue'])

const currentDate = ref(new Date(props.modelValue))

const weekDays = ['日', '一', '二', '三', '四', '五', '六']

const currentMonth = computed(() => {
  return `${currentDate.value.getFullYear()}年${currentDate.value.getMonth() + 1}月`
})

const calendarDates = computed(() => {
  const year = currentDate.value.getFullYear()
  const month = currentDate.value.getMonth()
  const firstDay = new Date(year, month, 1)
  const lastDay = new Date(year, month + 1, 0)
  const dates = []

  // Previous month days
  const prevMonthLastDay = new Date(year, month, 0).getDate()
  for (let i = firstDay.getDay() - 1; i >= 0; i--) {
    dates.push({
      key: `prev-${i}`,
      day: prevMonthLastDay - i,
      isCurrentMonth: false,
      isToday: false,
      isSelected: false,
      date: new Date(year, month - 1, prevMonthLastDay - i)
    })
  }

  // Current month days
  const today = new Date()
  for (let i = 1; i <= lastDay.getDate(); i++) {
    const date = new Date(year, month, i)
    dates.push({
      key: `current-${i}`,
      day: i,
      isCurrentMonth: true,
      isToday: date.toDateString() === today.toDateString(),
      isSelected: date.toDateString() === currentDate.value.toDateString(),
      date
    })
  }

  // Next month days
  const remainingDays = 42 - dates.length
  for (let i = 1; i <= remainingDays; i++) {
    dates.push({
      key: `next-${i}`,
      day: i,
      isCurrentMonth: false,
      isToday: false,
      isSelected: false,
      date: new Date(year, month + 1, i)
    })
  }

  return dates
})

function prevMonth() {
  currentDate.value = new Date(currentDate.value.getFullYear(), currentDate.value.getMonth() - 1, 1)
}

function nextMonth() {
  currentDate.value = new Date(currentDate.value.getFullYear(), currentDate.value.getMonth() + 1, 1)
}

function selectDate(date) {
  currentDate.value = date.date
  emit('update:modelValue', date.date)
}
</script>

<style scoped>
.glass-calendar {
  padding: 16px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.calendar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.calendar-nav {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.1);
  color: white;
  cursor: pointer;
  transition: all 0.2s ease;
}

.calendar-nav:hover {
  background: rgba(255, 255, 255, 0.2);
}

.calendar-title {
  font-size: 16px;
  font-weight: 600;
  color: white;
}

.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 4px;
}

.calendar-weekday {
  text-align: center;
  font-size: 12px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.5);
  padding: 8px 0;
}

.calendar-date {
  text-align: center;
  padding: 8px 0;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.7);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.calendar-date:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.calendar-date.is-today {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  font-weight: 600;
}

.calendar-date.is-selected {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
  font-weight: 600;
}

.calendar-date.is-other-month {
  opacity: 0.3;
}
</style>
