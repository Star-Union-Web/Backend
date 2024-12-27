let fields = document.querySelectorAll('form input');
console.log(fields);
try {
    document.querySelector('form #id_username').setAttribute('placeholder', 'Username');
    document.querySelector('form #id_password').setAttribute('placeholder', 'Password');
    document.querySelector('form #id_password1').setAttribute('placeholder', 'Password');
    document.querySelector('form #id_password2').setAttribute('placeholder', 'Confirm Password');
} catch {
    console.log(":(");
}
for (i = 0; i < fields.length; i++) {
    fields[i].classList.add('editText');
    if (fields[i].id == "id_username") {
        fields[i].setAttribute('placeholder', 'Username');
    }

    if (fields[i].id == "id_password") {
        fields[i].setAttribute('placeholder', 'Password');
    }

    if (fields[i].id == "id_password1") {
        fields[i].setAttribute('placeholder', 'Password');
    }

    if (fields[i].id == "id_password2") {
        fields[i].setAttribute('placeholder', 'Confirm Password');
    }
    //fields[i].setAttribute('placeholder', 'Username');
}
let spans = document.querySelectorAll('form span, label');
for (i = 0; i < spans.length; i++) {
    spans[i].style.display = "none";
}

let conditions = document.querySelectorAll('li');
for (i = 0; i < conditions.length; i++) {
    conditions[i].classList.add('conditions');
}

let errorlist = document.querySelectorAll('.errorlist');
//let errorlistChildren = errorslist.childNodes;
//console.log(errorlistChildren);
for (i = 0; i < errorlist.length; i++) {
    for (j=0; j< errorlist[i].childNodes.length; j++){
        errorlist[i].childNodes[j].classList.add("error");
    }
}