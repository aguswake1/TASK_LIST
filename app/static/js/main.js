$("document").ready(function(){
    setTimeout(function(){
        hide_alert();
    }, 1900);
});


function hide_alert()
{
    let alert = document.getElementsByClassName("alert")[0];

    if (typeof(alert) !== undefined && alert !== null) alert.style.display = 'none';
}