document.querySelector('.main').style.display='none';
        document.querySelector('#load').classList.add('loader');

        //SET TIMEOUT

        setTimeout(()=>{
            document.querySelector('.main').style.display='block';
            document.querySelector('#load').classList.remove('loader');
        },5000);

