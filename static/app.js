const userForm = document.querySelector('#user_form');
let users = [];
let editing = false;
let user_id = null;

window.addEventListener('DOMContentLoaded', async () => {
    const response = await fetch("/api/users");
    const data = await response.json();
    users = data;
    render_users(users);
})


userForm.addEventListener("submit", async (e) => {
    e.preventDefault()
    const username = userForm["user_input"].value
    const email = userForm["email_input"].value
    const password = userForm["pass_input"].value

    if (editing != true) {
        const response = await fetch("/api/users", {
            method: "POST",
            headers: {
                "Content-Type": "aplication/json",
            },
            body: JSON.stringify({
                username,
                email,
                password,
            }),
        });
        const data = await response.json();
        users.unshift(data);
    } else {
        
        await fetch(`/api/users/${user_id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "aplication/json",
            },
            body: JSON.stringify({
                username,
                email,
                password,
            }),
        });
        const update_user = await response.json();
        users = user.map(user => user.id === update_user.id ? update_user : user);
        render_users(users);
        editing = false;
        user_id = null;
    }

    render_users(users)
    userForm.reset();
});


function render_users(users) {
    const user_list = document.querySelector('#user_list');
    users.forEach(user => {
        const user_item = document.createElement('li')
        user_item.classList = 'list-group-item'
        user_item.innerHTML = `<header><b>User:</b> ${user.username}
        <p class="text-truncate"><b>Email:</b> ${user.email}</p>
        <footer>
        <button class="btn-edit btn btn-secondary btn-sm">Edit</button>
        <button class="btn-delete btn btn-danger btn-sm">Delete</button>
        </footer>`

        // To delete
        const btn_delete = user_item.querySelector('.btn-delete')
        btn_delete.addEventListener('click', async () => {
            const response = await fetch(`/api/users/${user.id}`, {
                method: 'DELETE',
            })
            const data = await response.json()
            users = users.filter(user => user.id !== data.id)
            render_users(users)
        })


        // To Update
        const btn_edit = user_item.querySelector('.btn-edit')

        btn_edit.addEventListener('click', async (e) => {
            const response = await fetch(`/api/users/${user.id}`)
            const data = await response.json()

            userForm["user_input"].value = data.username;
            userForm["email_input"].value = data.email;
            editing = true;
            user_id = data.id;
        })

        user_list.append(user_item)
    });
}