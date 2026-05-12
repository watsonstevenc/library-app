//this is the list of books that will populate in the page
const books = [
    { title: "Inspired", author: "Marty Cagan", description: "The Agile and OKR playbook for developing tech products"    },
    { title: "The 21 Irrefutable Laws of Leadership", author: "John Maxwell", description: "The leadership playbook on how to lead teams and get better"    },
    { title: "Good to Great", author: "Jim Collins", description: "What differentiates the truly great companies from just good"    }
]

//we look for the book-list element in the html so we know where to put the data
const bookTableBody = document.getElementById("book-list")

//for each "book" line in the books variable, we create a table row and set the data for each column and then append it
books.forEach(book => {
    const row = document.createElement("tr")
    row.innerHTML = `<td>${book.title}</td><td>${book.author}</td><td>${book.description}</td>`
    bookTableBody.appendChild(row)
})