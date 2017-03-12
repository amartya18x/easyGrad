[![Build Status](https://travis-ci.org/amartya18x/easyGrad.svg?branch=master)](https://travis-ci.org/amartya18x/easyGrad)
# Easy Grad

This library aims to provide an easy implementation of doing symbolic operations in python

## Testing

```python 
   def test1():
      x = Integer("Int1")
      y = Integer("Int2")
      z = Integer("Int3")
      p = Integer("Int4")
      k = p + z
      kd = k * 2
      t = x - kd
      td = t - 2
      s = td * z
      sd = s / 5
      graph = GradGraph(sd)
      output = graph.getOutput({x: 36,
                              y: 2,
                              z: 3,
                              p: 9})
      assert (output == 6), "Output : "+str(output)```

