document.addEventListener('DOMContentLoaded', () => {
    const postsContainer = document.getElementById('posts-container');
    const prevPageBtn = document.getElementById('prev-page');
    const nextPageBtn = document.getElementById('next-page');
    const currentPageSpan = document.getElementById('current-page');

    const posts = [
        {
            id: 1,
            title: 'First Blog Post',
            excerpt: 'This is a short excerpt of the first blog post...',
            author: 'John Doe',
            date: 'Dec 10, 2024'
        },
        {
            id: 2,
            title: 'Another Interesting Post',
            excerpt: 'Another exciting blog post about something amazing...',
            author: 'Jane Smith',
            date: 'Dec 9, 2024'
        },
        // Add more posts as needed
    ];

    let currentPage = 1;
    const postsPerPage = 5;

    function displayPosts() {
        postsContainer.innerHTML = ''; // Clear previous posts
        
        const startIndex = (currentPage - 1) * postsPerPage;
        const endIndex = startIndex + postsPerPage;
        const displayedPosts = posts.slice(startIndex, endIndex);

        displayedPosts.forEach(post => {
            const postElement = document.createElement('div');
            postElement.classList.add('post-card');
            postElement.innerHTML = `
                <h3>${post.title}</h3>
                <div class="post-meta">
                    <span>By ${post.author}</span>
                    <span>${post.date}</span>
                </div>
                <p>${post.excerpt}</p>
                <a href="post-detail.html?id=${post.id}" class="read-more">Read More</a>
            `;
            postsContainer.appendChild(postElement);
        });

        currentPageSpan.textContent = `Page ${currentPage}`;
        updatePaginationButtons();
    }

    function updatePaginationButtons() {
        prevPageBtn.disabled = currentPage === 1;
        nextPageBtn.disabled = currentPage * postsPerPage >= posts.length;
    }

    prevPageBtn.addEventListener('click', () => {
        if (currentPage > 1) {
            currentPage--;
            displayPosts();
        }
    });

    nextPageBtn.addEventListener('click', () => {
        if (currentPage * postsPerPage < posts.length) {
            currentPage++;
            displayPosts();
        }
    });

    // Initial display
    displayPosts();
});