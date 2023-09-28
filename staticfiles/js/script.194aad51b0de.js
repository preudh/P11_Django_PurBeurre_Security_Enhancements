// erase img border when no product found search.html

let border_search;
border_search = document.getElementById("back_img");


function eraseBorder (border_search) {
        if (border_search.outerText === "")
    {
        border_search.style.borderStyle = "none";
    }
}

eraseBorder(border_search);




