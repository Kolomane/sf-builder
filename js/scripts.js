///////////////////////////////
// LISTENERS //////////////////
///////////////////////////////

// Flip Icon - Import a jQuery event Listener AFTER loading Conditions
$('[id$="-expand"]').on('click', function (event) {
    console.log(`clicked the thing | name = ${event.target.parentElement.id}`)
    flipIcon(`${event.target.id}`)
})

function flipIcon(name) {
    console.log(`flipicon | name = ${name}`)
    let theButton = $(`${name}`);
    if (theButton.html() == '<i class="bi bi-arrow-bar-up"></i>') {
        theButton.html('<i class="bi bi-arrow-bar-down"></i>')
    } else {
        theButton.html('<i class="bi bi-arrow-bar-up"></i>')
    }
}