let n = 1

function gallery(num){
    // 5 이상이 되면 1로 갈 수 있도록 프로그램하시오.
    // 1이하가 되면 5로 변경될 수 있도록 프로그램 하시오.
    n += num;
    if(n>5){
        n=1
    }else if(n<1){
        n=5
    }
    
    

    //let a = document.getElementById("photo").getAttribute("src")
    let a = document.getElementById("photo")
    a.setAttribute("src","images/"+n+".jpg")
    //                    images/2.jpg
    document.getElementById('viewNum').innerText=n;


}





/* let adminId = 'admin';
let adminPw = '1111';


function loginBtn(){
    let uid = prompt('아이디를 입력하세요.');
    let upw = prompt('패스워드를 입력하세요.');
    
    loginBtn(uid,upw); //login 함수호출(매개변수 전달)
}


function loginBtn(uid,upw){
    if(uid == adminId && upw == adminPw){
        alert('로그인 성공!')
        location.href='http://www.naver.com'; //로그인 성공시 이동
    }
    else{
        alert('아이디 또는 패스워드가 일치하지 않습니다. 다시 입력하세요.')
    }

} */


/* function sum1(){
    let sum = 0;
    let a = parseInt(prompt('숫자를 입력하세요.'));
    let b = parseInt(prompt('숫자를 입력하세요.'));
    // 1, 10을 입력 했을때 1부터 10까지 있는 합을 출력.
    
    for(let i=a; i<=b; i++){
        sum += i;

    }

    document.write(a+'부터'+b+'까지의 합은 : '+sum);
} */