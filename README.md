# Error encoder

Some implementations of various error-correcting codes

## Hamming code

Implementation of a [Hamming code](https://en.wikipedia.org/wiki/Hamming_code), generalized as `(n, k)`. Works as follows

```python
long_binary_message = np.random.randint(2, size=40)

encoded = composite_encoder(long_binary_message)
decoded = composite_decoder(encoded, 4)
```
