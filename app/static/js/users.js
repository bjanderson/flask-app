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

    users.forEach(user => {
        addUserToTable(user)
    })
}

function addUserToTable(user) {
    const tbody = document.querySelector('#users_table_body')
    const userRow = getUserRow(user)
    tbody.appendChild(userRow)
}

function getUserRow(user) {
    const userTemplate = document.querySelector('#user_row_template').content.cloneNode(true)

    const name = userTemplate.querySelector('.name')
    name.innerText = user.name
    name.addEventListener('click', () => { editUser(user) })

    const email = userTemplate.querySelector('.email')
    email.innerText = user.email

    const pk = userTemplate.querySelector('.pk')
    pk.innerText = user.pk

    const deleteButton = userTemplate.querySelector('.user-buttons')
    deleteButton.addEventListener('click', () => { deleteUser(user) })
    deleteButton.innerText = 'X'

    return userTemplate
}

function addUser() {
    const nameInput = document.querySelector('#username')
    const emailInput = document.querySelector('#useremail')

    const name = nameInput.value
    const email = emailInput.value

    if (name && email) {
        const user = {
            name: name,
            email: email
        }

        const api = 'http://localhost:5000/user'
        const options = {
            method: 'POST',
            body: JSON.stringify(user)
        }
        fetch(api, options)
            .then(response => response.json())
            .then(user => {
                console.log(user)
                addUserToTable(user)
            })
            .catch((error) => { console.log(error) })
    } else {
        alert('Enter name and email')
    }
}

function updateUser(userToEdit) {
    console.log('updateUser')
    const nameInput = document.querySelector('#username')
    const emailInput = document.querySelector('#useremail')

    const name = nameInput.value
    const email = emailInput.value

    if (name && email) {
        const user = {
            name: name,
            email: email,
            pk: userToEdit.pk
        }

        const api = `http://localhost:5000/user/${userToEdit.pk}`
        const options = {
            method: 'PUT',
            body: JSON.stringify(user)
        }
        fetch(api, options)
            .then(response => response.json())
            .then(user => {
                console.log(user)
                clearTable()
                getUsers()
            })
            .catch((error) => { console.log(error) })
    } else {
        alert('Enter name and email')
    }
}

function clearTable() {
    const tbody = document.querySelector('#users_table_body')
    tbody.innerHTML = ''
}

function editUser(user) {
    console.log(user)

    const nameInput = document.querySelector('#username')
    const emailInput = document.querySelector('#useremail')

    nameInput.value = user.name
    emailInput.value = user.email

    addEditButton(user)
}

function addEditButton(user) {

    const buttonsDiv = document.querySelector('.buttons')
    buttonsDiv.innerHTML = ''

    const editButton = document.createElement('button')
    editButton.innerText = 'Edit'
    editButton.addEventListener('click', () => { updateUser(user) })

    buttonsDiv.appendChild(editButton)
}

function deleteUser(user) {
    console.log('deleteUser')

    const api = `http://localhost:5000/user/${user.pk}`
    const options = {
        method: 'DELETE'
    }
    fetch(api, options)
        .then(() => {
            clearTable()
            getUsers()
        })
        .catch((error) => { console.log(error) })

}
