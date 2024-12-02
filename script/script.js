function validarSenha() {
    var senha = document.getElementById("password").value;
    // Verificando se a senha tem pelo menos 6 caracteres
    if (senha.length < 6) {
        alert("A senha deve ter pelo menos 6 caracteres.");
        return false;
    }
    return true;
}