function shiftChar(c, shift) {
  const code = c.charCodeAt(0);

  if (code >= 65 && code <= 90) {
    return String.fromCharCode(((code - 65 + shift + 26) % 26) + 65);
  } else if (code >= 97 && code <= 122) {
    return String.fromCharCode(((code - 97 + shift + 26) % 26) + 97);
  } else {
    return c;
  }
}

function transformMessage(message, shift) {
  return message.split("").map(char => shiftChar(char, shift)).join("");
}

function encodeMessage() {
  const message = document.getElementById("message").value;
  const shift = parseInt(document.getElementById("shift").value);
  const encoded = transformMessage(message, shift);
  document.getElementById("output").innerText = encoded;
}

function decodeMessage() {
  const message = document.getElementById("message").value;
  const shift = parseInt(document.getElementById("shift").value);
  const decoded = transformMessage(message, -shift);
  document.getElementById("output").innerText = decoded;
}

function clearAll() {
  document.getElementById("message").value = "";
  document.getElementById("shift").value = 3;
  document.getElementById("output").innerText = "";
}
