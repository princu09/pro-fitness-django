function changeImg(smallImg) {
    var fullImg = document.getElementById("imageBox");
    fullImg.src = smallImg.src;
}

$(document).ready(function() {
    rate = []
    rating = $('.rating').text();
    for (let i = 0; i < rating; i++) {
        rate.push('<i class="fas fa-star"></i>')
    }
    if (rate.length < 5) {
        addBlankStar = 5 - rate.length
        for (let i = 0; i < addBlankStar; i++) {
            rate.push('<i class="fal fa-star"></i>')
        }
        $('.rating').html(rate);
    }

    // Wishlist 

    $('.whishlist-btn').on('click', function() {
        var _pid = $(this).attr('data-product');
        var _vm = $(this);
        $.ajax({
            url: "/add_wishlist",
            data: {
                product: _pid
            },
            dataType: "json",
        });
    })

    // // Cart

    $('.btn-cart').on('click', function() {
        var _pid = $(this).attr('data-product');
        var _cartItem = $('.itemLen').val();
        $.ajax({
            url: "/add_cart",
            data: {
                product: _pid,
                cartItem: _cartItem,
            },
            dataType: "json",
            success: function(response) {
                $('.itemLen').val(0);
            }
        });
    })

    $('.add_cart_from_wishlist').on('click', function() {
        var _pid = $(this).attr('data-product');
        var _cartItem = 1;
        $.ajax({
            url: "/add_cart",
            data: {
                product: _pid,
                cartItem: _cartItem,
            },
            dataType: "json",
            success: function(response) {
                window.location = '/removeFromWishlist/' + _pid;
            }
        });
    })

})