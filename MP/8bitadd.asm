.8086
.model small
.data
num1 db 09h
num2 db 04h
sum db ?
.code
start:
mov ax, @data
mov ds, ax
mov al, num1
add al, num2
mov sum, al
mov ah, 4ch
int 21h
end start