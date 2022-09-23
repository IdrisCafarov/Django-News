let toggle = document.querySelectorAll("#toggle");
let toggle_a = document.querySelectorAll("#toggle_a");
let media_id = document.querySelectorAll("#media_id");
let view_all_id = document.getElementById("view_all_id");

view_all_id.addEventListener('click', () => {
    [...media_id].map((media) => {
        media.classList.toggle("media_block_none")
        console.log("uhfushf")
    })
});
// [...toggle].map((tog) => {
//     tog.addEventListener("click", () => {
//         console.log('click');
//         tog.classList.add("color_toggle");
//     })
// })
// console.log("salam");




// console.log(comments);