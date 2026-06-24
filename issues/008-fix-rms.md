# Fix rms()

`rms()` in `habitat/calc.py` should return the root mean square, not the arithmetic mean.

## Expected

```python
rms([1.0, 2.0, 2.0])  # → sqrt(3) ≈ 1.732050808
```

## Failing test

```bash
pytest tests/test_calc.py::test_rms -x
```