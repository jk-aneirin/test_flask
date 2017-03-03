window.onload=function(){
    var pwd1=document.pwdForm.pwd1;
    var pwd2=document.pwdForm.pwd2;
    var check=document.getElementById("subBut");
    function isPass(pwd1,pwd2){
        if(pwd1!=pwd2){
            alert("Do Not Match The Password Input");
            }
        }
        check.onclick=function(){
            isPass(pwd1.value,pwd2.value);
            }
    }
