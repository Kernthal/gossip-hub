export function isValidEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return re.test(email)
}

export function isValidPassword(password) {
  return password.length >= 6
}

export function isValidUsername(username) {
  return username.length >= 2 && username.length <= 20
}

export function isValidUrl(url) {
  try {
    new URL(url)
    return true
  } catch {
    return false
  }
}

export function isNotEmpty(value) {
  return value && value.trim().length > 0
}

export function maxLength(value, max) {
  return value.length <= max
}

export function minLength(value, min) {
  return value.length >= min
}
