# ----------------------------------------------------------------------------------------
# Writes "Hello, World" to the console using only system calls. Runs on 64-bit Linux only.
# To assemble and run:
#
#     gcc -c hello.s && ld hello.o && ./a.out
#
# or
#
#     gcc -nostdlib hello.s && ./a.out
# ----------------------------------------------------------------------------------------

        .global mult3

        .text
mult3:
        mov     %rdi, %rax                # result (rax) initially holds x
        imul   %rsi, %rax                # if so, set result to y
        imul   %rdx, %rax                # if so, set result to z
        ret                               # the max will be in eax
