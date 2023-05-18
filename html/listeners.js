///////////////////////////////
// ACTIONS ////////////////////
///////////////////////////////

// Action Toggles
var theLength = ($(`#initiativeList input:radio`).length) - 1
var initiativeCount = 0
var updateRoundCount = false
$('button[id="initiativeAdvance"]').on("click", function (event) {
    if (updateRoundCount) {
        $('#roundCount').text(Number($('#roundCount').text()) + 1)
        updateRoundCount = false
    }
    $(`#initiativeList input:radio`).each(function (index, element) {
        if ($(this).is(':checked')) {
            initiativeCount = index
            if (index == theLength) {
                initiativeCount = -1
            }
        }
        let thePC = $(this).siblings().text();
        if (index < theLength) {
            if (index == (initiativeCount + 1)) {
                $(this).prop('checked', true);
            }
        }
        if (index == theLength) {
            if (index == (initiativeCount + 1)) {
                $(this).prop('checked', true);
                initiativeCount = -1
                updateRoundCount = true
            }
        }
    });
});