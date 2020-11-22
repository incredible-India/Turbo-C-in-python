console.log("Himanshu kumar sharma")
    
var ledoc=document.getElementsByClassName('mainpara')
    
ledoc[0].addEventListener('mouseover',()=>{
    ledoc[0].style.color="blue"
})
ledoc[0].addEventListener('mouseleave',()=>{
    ledoc[0].style.color="green"
})
// ledoc[0].previousElementSibling[