
document.getElementById('load-more-btn').addEventListener('click', function() {
    // Create new post element
    const newPost = document.createElement('div');
    newPost.classList.add('post');
    newPost.style.cssText = "background: rgba(0, 0, 0, 0.7); margin: 20px 0; padding: 15px; border-radius: 10px; width: 90%; max-width: 400px; color: white; text-align: center;";
    
    // Populate new post with content
    newPost.innerHTML = `
        <div style="font-weight: bold; margin-bottom: 10px;">Jane Smith</div>
        <div style="border: 2px solid white; border-radius: 10px; overflow: hidden; margin: 10px 0;">
            <img src="{% static 'images/photo2.webp' %}" alt="Post Image" style="width: 100%; display: block;">
        </div>
        <div style="font-size: 1.2rem; font-weight: bold; margin-top: 10px;">Another Post</div>
        <div style="font-size: 0.9rem; color: #ccc; margin-top: 5px;">Uploaded on: 2024-12-11</div>
    `;
    
    // Append the new post to the container
    document.getElementById('post-container').appendChild(newPost);
});
