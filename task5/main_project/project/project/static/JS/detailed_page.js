document.addEventListener('DOMContentLoaded', () => {
    const postTitle = document.getElementById('post-title');
    const postAuthor = document.getElementById('post-author');
    const postDate = document.getElementById('post-date');
    const postContent = document.getElementById('post-content');
    const commentsContainer = document.getElementById('comments-container');
    const commentForm = document.getElementById('comment-form');
    const commentText = document.getElementById('comment-text');

    // Simulated post and comments data
    const post = {
        id: 1,
        title: 'Detailed Blog Post',
        content: 'This is the full content of the blog post. It can be multiple paragraphs long and provide in-depth information about the topic.',
        author: 'John Doe',
        date: 'Dec 10, 2024'
    };

    const comments = [
        { 
            id: 1, 
            author: 'Alice', 
            content: 'Great post!', 
            date: 'Dec 10, 2024' 
        },
        { 
            id: 2, 
            author: 'Bob', 
            content: 'Very informative.', 
            date: 'Dec 11, 2024' 
        }
    ];

    // Populate post details
    postTitle.textContent = post.title;
    postAuthor.textContent = post.author;
    postDate.textContent = post.date;
    postContent.innerHTML = `<p>${post.content}</p>`;

    // Display comments
    function displayComments() {
        commentsContainer.innerHTML = ''; // Clear existing comments
        comments.forEach(comment => {
            const commentElement = document.createElement('div');
            commentElement.classList.add('comment');
            commentElement.innerHTML = `
                <div class="comment-header">
                    <span class="comment-author">${comment.author}</span>
                    <span class="comment-date">${comment.date}</span>
                </div>
                <p class="comment-content">${comment.content}</p>
            `;
            commentsContainer.appendChild(commentElement);
        });
    }

    // Handle comment submission
    commentForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const newComment = {
            id: comments.length + 1,
            author: 'Current User', // In a real app, this would be the logged-in user
            content: commentText.value,
            date: new Date().toLocaleDateString()
        };

        comments.push(newComment);
        displayComments();
        commentText.value = ''; // Clear the textarea
    });

    // Initial comment display
    displayComments();
});