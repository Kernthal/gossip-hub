import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  const user = ref(null)
  const token = ref(localStorage.getItem('token') || '')
  const isLoggedIn = computed(() => !!token.value)

  async function login(email, password) {
    // TODO: 调用登录 API
    const response = await fetch('/api/users/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    })
    const data = await response.json()
    token.value = data.token
    user.value = data.user
    localStorage.setItem('token', data.token)
  }

  async function register(userData) {
    // TODO: 调用注册 API
    const response = await fetch('/api/users/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    })
    const data = await response.json()
    token.value = data.token
    user.value = data.user
    localStorage.setItem('token', data.token)
  }

  function logout() {
    token.value = ''
    user.value = null
    localStorage.removeItem('token')
  }

  async function fetchUser() {
    if (!token.value) return
    // TODO: 调用获取用户信息 API
    const response = await fetch('/api/users/me', {
      headers: { 'Authorization': `Bearer ${token.value}` }
    })
    user.value = await response.json()
  }

  return { user, token, isLoggedIn, login, register, logout, fetchUser }
})

export const usePostStore = defineStore('post', () => {
  const posts = ref([])
  const currentPost = ref(null)
  const loading = ref(false)
  const error = ref(null)

  async function fetchPosts(params = {}) {
    loading.value = true
    error.value = null
    try {
      // TODO: 调用获取帖子 API
      const response = await fetch(`/api/posts?${new URLSearchParams(params)}`)
      posts.value = await response.json()
    } catch (e) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  async function fetchPost(id) {
    loading.value = true
    error.value = null
    try {
      // TODO: 调用获取帖子详情 API
      const response = await fetch(`/api/posts/${id}`)
      currentPost.value = await response.json()
    } catch (e) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  async function createPost(postData) {
    loading.value = true
    error.value = null
    try {
      // TODO: 调用创建帖子 API
      const response = await fetch('/api/posts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData)
      })
      const newPost = await response.json()
      posts.value.unshift(newPost)
      return newPost
    } catch (e) {
      error.value = e.message
      throw e
    } finally {
      loading.value = false
    }
  }

  async function likePost(id) {
    // TODO: 调用点赞 API
    await fetch(`/api/posts/${id}/like`, { method: 'POST' })
    const post = posts.value.find(p => p.id === id)
    if (post) post.likes++
  }

  return { posts, currentPost, loading, error, fetchPosts, fetchPost, createPost, likePost }
})

export const useCircleStore = defineStore('circle', () => {
  const circles = ref([])
  const currentCircle = ref(null)
  const loading = ref(false)

  async function fetchCircles() {
    loading.value = true
    try {
      // TODO: 调用获取圈子 API
      const response = await fetch('/api/circles')
      circles.value = await response.json()
    } finally {
      loading.value = false
    }
  }

  async function createCircle(circleData) {
    // TODO: 调用创建圈子 API
    const response = await fetch('/api/circles', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(circleData)
    })
    const newCircle = await response.json()
    circles.value.push(newCircle)
    return newCircle
  }

  return { circles, currentCircle, loading, fetchCircles, createCircle }
})
