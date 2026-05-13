//editing variable (null is add, number is edit)
let editingIndex = null

//we connect the book-list table in the html to the bookTableBody variable
const bookTableBody = document.getElementById("book-list")

//create a function renderBooks that creates records of title/author/description for each book
function renderBooks(books) {
    bookTableBody.innerHTML = "" // clear existing rows first
    books.forEach((book, index) => {
        const row = document.createElement("tr")
        row.innerHTML = `
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${book.description}</td>
            <td><button onclick="deleteBook(${index})">Delete</button></td>
            <td><button onclick="editBook(${index})">Edit</button></td>
            `
        bookTableBody.appendChild(row)
    })
}  

//create a function to delete books
function deleteBook(index) {
    fetch(`http://127.0.0.1:5000/books/${index}`, {
        method: "DELETE"
    })
    .then(() => fetch("http://127.0.0.1:5000/books"))
    .then(response => response.json())
    .then(data => renderBooks(data))
}

//create a function to edit books
function editBook(index) {
    fetch("http://127.0.0.1:5000/books")
        .then(response => response.json())
        .then(books => {
            const book = books[index]
            document.getElementById("input-title").value = book.title
            document.getElementById("input-author").value = book.author
            document.getElementById("input-description").value = book.description
            editingIndex = index
        })
}

//call function to populate the books on load
fetch("http://127.0.0.1:5000/books")
    .then(response => response.json())
    .then(data => renderBooks(data))

//create a listener on the book-form submit action to get inputs and update the table.
document.getElementById("book-form").addEventListener("submit", function(event) {

    event.preventDefault() //stops auto refresh

    //get inputs from the form
    const title = document.getElementById("input-title").value
    const author = document.getElementById("input-author").value
    const description = document.getElementById("input-description").value

    //update books
    if (editingIndex !== null) {
        fetch(`http://127.0.0.1:5000/books/${editingIndex}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title, author, description })
        })
        .then(() => fetch("http://127.0.0.1:5000/books"))
        .then(response => response.json())
        .then(data => renderBooks(data))
        editingIndex = null
    } else {
        fetch("http://127.0.0.1:5000/books", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title, author, description })
        })
        .then(() => fetch("http://127.0.0.1:5000/books"))
        .then(response => response.json())
        .then(data => renderBooks(data))
    }

    //reset the form
    document.getElementById("book-form").reset()

})