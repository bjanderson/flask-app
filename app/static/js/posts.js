
function getPosts() {
    console.log('getPosts()')
    const api = 'http://localhost:5000/post'
    fetch(api) // executes a GET request by default
        .then(response => response.json())
        .then(posts => {
            addPosts(posts)
        })
        .catch((error) => { console.log(error) });
}

getPosts()

function addPosts(posts) {
    console.log('addPosts')
    posts.forEach(post => {
        addPost(post)
    })
}

function addPost(post) {
    const postTemplate = document.querySelector('#post_template').content.cloneNode(true)

    const title = postTemplate.querySelector('.title')
    title.innerText = post.title

    const content = postTemplate.querySelector('.content')
    content.innerText = post.content

    const postsDiv = document.getElementById('posts')
    postsDiv.appendChild(postTemplate)
}
