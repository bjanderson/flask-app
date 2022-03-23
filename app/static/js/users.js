// JavaScript Fetch API - https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch

// immediately run the getUsers function when this file loads...
getUsers()

function getUsers() {
    console.log('getUsers()')
    const api = 'http://localhost:5000/user'
    fetch(api) // executes a GET request by default
        .then(response => response.json())
        .then(users => {
            addUsersToTable(users)
        })
        .catch((error) => { console.log(error) });
}

function addUsersToTable(users) {
    console.log(users)

    const tbody = document.querySelector('#users_table_body')

    users.forEach(user => {
        const userRow = getUserRow(user)
        tbody.appendChild(userRow)
    })
}

function getUserRow(user) {
    const userTemplate = document.querySelector('#user_row_template').content.cloneNode(true)

    const name = userTemplate.querySelector('.name')
    name.innerText = user.name

    const email = userTemplate.querySelector('.email')
    email.innerText = user.email

    const pk = userTemplate.querySelector('.pk')
    pk.innerText = user.pk

    userTemplate.querySelector('tr').addEventListener('click', () => { console.log(user) })

    return userTemplate
}
