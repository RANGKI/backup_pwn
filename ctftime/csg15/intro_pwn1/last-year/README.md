This is an introductory challenge for exploiting Linux binaries with memory corruptions. Nowadays there are quite a few mitigations that make it not as straight forward as it used to be.
So in order to introduce players to pwnable challenges, [LiveOverflow created a video walkthrough](https://www.youtube.com/watch?v=hhu7vhmuISY) of the first challenge.

This challenge was already featured in last year's CSCG. We are aware that public writeups exist, but we figured this challenge is still a nice-to-have for newcomers, so we released it again.

*Note*: The video writeup of LiveOverflow is not completely functional. To give you hint: It's about the address of the `ret` instruction that was chosen to re-align the stack.

Suppose `ASLR` is rather 'smooth' - meaning a whole bunch of nibbles are zero - (which is pretty much always the case in our setup) all addresses within the offset range of `0xa00` to `0xaff`
translate to addresses looking like `xxxxxxxxxx0axx`, requiring you to send the bytes `xx xx xx xx xx xx 0a xx` over the wire. Now the problem with this is that `0a` is a newline (`\\n`), which in turn terminates `gets()` (refer to `man 3 gets`), meaning that your payload terminates prematurely.