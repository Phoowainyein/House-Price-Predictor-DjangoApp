export const addUserToLocalStorage = (userInfo) => {
  localStorage.setItem('user', JSON.stringify(userInfo))
}

export const removeUserFromLocalStorage = () => {
  localStorage.removeItem('user')
}

export const getUserFromLocalStorage = () => {
  const result = localStorage.getItem('user')
  return result ? JSON.stringify(result) : null
}
