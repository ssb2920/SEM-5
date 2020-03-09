.8086
.model small
.data
num1 db 07h
num2 db 03h
result dw ?
.code
start:
	mov ax, @data
	mov ds, ax
	mov al, num1
	mov ah, 00h
	mov bl, num2
	div bl
	mov result, ax
	int 3h
	mov ah, 4ch
	int 21h
	end start

