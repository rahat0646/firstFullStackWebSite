var comment = document.getElementById('comment')
var rating = document.querySelectorAll('.rating-group input')
var comment_error = document.getElementById('comment_error')
var rating_error = document.getElementById('rating_error')


function validateReview() {
    if (comment.value.length <= 1 ) {
        comment_error.style.display = "block";
        comment.focus();
        return false
    }
    if (rating.values <= 1) {
        rating_error.style.display = "block";
        return false
    }
}
