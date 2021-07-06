
// Efectos generales DOM
function CambiarMayusculasContacto()
{
    var a = document.getElementById('nomzap');
    a.value = a.value.toUpperCase();
}

function CambiarMayusculasMarca()
{
    var a = document.getElementById('marca');
    a.value = a.value.toUpperCase();
}

function CambiarMayusculas()
{
    var a = document.getElementById('nom');
    a.value = a.value.toUpperCase();
}


// Validación de Sesión

function validacion()
{
    nom= document.getElementById('nom').value;
    email = document.getElementById('ema').value;
    fono = document.getElementById('fono').value;
    pass = document.getElementById('pass').value;
    checkbox = document.getElementById("checkbox1");

    if(nom == null || nom.length<=5 || /^\s+$/.test(nom))
    {
        alert('Debe ingresar un Nombre de Usuario de 5 carácteres mínimo...');
        document.getElementById('nom').value="";
        document.datos.nom.focus();
        return false;
    }

    
    if(email == null || email.length==0 || /^\s+$/.test(email))
    {
        alert('Debe ingresar un Correo...');
        document.getElementById('ema').value="";
        document.datos.ema.focus();
        return false;
    }

    if(!(/^\d{9}$/.test(fono)) )
    {
        alert('Debe ingresar un teléfono de 9 dígitos');
        document.getElementById('fono').value="";
        document.datos.fono.focus();
        return false;
    }   

    if(pass == null || pass.length<8 || /^\s+$/.test(pass))
    {
        alert('Debe ingresar una contraseña de 8 carácteres mínimo...');
        document.getElementById('pass').value="";
        document.datos.pass.focus();
        return false;
    }
    
    if (checkbox.checked){
    }
    else
    {
        alert("Debe aceptar los término y condiciones para poder registrarse...");
        return false;
    }
    return true;      
}


// Validación de aporte
function validacionAporte()
{
    nomzap = document.getElementById('nomzap').value;
    marca = document.getElementById('marca').value;
    val = document.getElementById('val').value;

    if(nomzap == null|| nomzap.length==0 ||/^\s+$/.test(nomzap))
    {
        alert('Debe ingresar el Nombre de la Zapatilla...');
        document.getElementById('nomzap').value="";
        document.datos.nomzap.focus();
        return false;
    }

    if(/^\s+$/.test(marca))
    {
        alert('Debe una marca de Zapatilla válida...');
        document.getElementById('marca').value="";
        document.datos.marca.focus();
        return false;
    }

    if(isNaN(val))
    {
        alert('Debe ingresar un valor válido...');
        document.getElementById('val').value="";
        document.datos.val.focus();
        return false;
    }
    return true;      
}




