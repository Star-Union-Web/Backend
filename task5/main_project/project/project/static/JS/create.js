document.addEventListener('DOMContentLoaded', () => {
    const createPostForm = document.getElementById('create-post-form');
    const postTitleInput = document.getElementById('post-title');
    const postContentInput = document.getElementById('post-content');
    const cancelPostButton = document.getElementById('cancel-post');

    // Simulated posts array (in a real app, this would be stored in a backend)
    const posts = [];

    createPostForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const newPost = {
            id: posts.length + 1,
            title: postTitleInput.value,
            content: postContentInput.value,
            author: 'Current User', // In a real app, this would be the logged-in user
            date: new Date().toLocaleDateString()
        };

        posts.push(newPost);

        // In a real application, you would send this to a backend
        console.log('New post created:', newPost);

        // Reset form
        postTitleInput.value = '';
        postContentInput.value = '';

        // Optionally redirect to homepage or show a success message
        alert('Post created successfully!');
    });

    cancelPostButton.addEventListener('click', () => {
        // Confirm cancellation
        if (confirm('Are you sure you want to cancel? Any unsaved changes will be lost.')) {
            postTitleInput.value = '';
            postContentInput.value = '';
        }
    });
});