    $(document).ready(function() {
        $(".menu-icon").on("click", function() {
            $("nav ul").toggleClass("showing");
        });
    });

    // Scrolling Effect

    $(window).on("scroll", function() {
        if($(window).scrollTop()) {
            $('nav').addClass('black');
        }

        else {
            $('nav').removeClass('black');
        }
    })

    function goto_github()
    {
        location.href = "https://github.com/Thionazin";
    }

    function goto_linkedin()
    {
        location.href = "https://www.linkedin.com/in/senhe-hao-7548841a8";
    }