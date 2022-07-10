let heart_attack_q = document.getElementById("heart_attack")
let stroke_q = document.getElementById("stroke")
let tia_q = document.getElementById("tia")
let cardio_surgery_q = document.getElementById("cardio_surgery")
let diabetes_q = document.getElementById("diabetes")
let insulin_q = document.getElementById("insulin")
let cancer_q = document.getElementById("cancer")

// Event handler function to toggle hidden status of each duration select field
function toggle_hidden(event, label_id, field_id) {
    let label = document.getElementById(label_id)
    let field = document.getElementById(field_id)
    if ((label.hidden == true) && (field.hidden == true)) {
        label.hidden = false
        field.hidden = false
    }
    else {
        label.hidden = true
        field.hidden = true
    }
}

function toggle_div_hidden(event, div_id) {
    let div = document.getElementById(div_id)
    if (div.hidden == true) {
        div.hidden = false
    }
    else {
        div.hidden = true
    }
}

// Event listeners
heart_attack_q.addEventListener("click", (event) => toggle_hidden(event, "heart_attack_dur_lbl", "heart_attack_dur"))
stroke_q.addEventListener("click", (event) => toggle_hidden(event, "stroke_dur_lbl", "stroke_dur"))
tia_q.addEventListener("click", (event) => toggle_hidden(event, "tia_dur_lbl", "tia_dur"))
cardio_surgery_q.addEventListener("click", (event) => toggle_hidden(event, "cardio_surgery_dur_lbl", "cardio_surgery_dur"))
diabetes_q.addEventListener("click", (event) => toggle_hidden(event, "insulin_lbl", "insulin"))
diabetes_q.addEventListener("click", (event) => toggle_hidden(event, "complications_lbl", "complications"))
insulin_q.addEventListener("click", (event) => toggle_hidden(event, "insulin_dur_lbl", "insulin_dur"))
cancer_q.addEventListener("click", (event) => toggle_div_hidden(event, "cancer_more"))
// Alternate implementation to toggle hidden attribute of cancer_more div, using lambda function, 
// opted for named func above for potential reusability
// cancer_q.addEventListener(
//    "click",
//    function() {
//        let div = document.getElementById("cancer_more")
//        if (div.hidden == true) {
//            div.hidden = false
//        }
//        else {
//            div.hidden = true
//       }
//    }
//)
