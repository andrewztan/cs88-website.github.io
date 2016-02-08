test = {
  'name': 'First',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def first(x):
          ...     x += 8
          ...     def second(y):
          ...         print('second')
          ...         return x + y
          ...     print('first')
          ...     return second
          >>> f = first(15)
          0cd62462fa747373868997245aecd4b2
          # locked
          >>> f
          72770592b08c5e54b6e1a45121cf7b3a
          # locked
          >>> f(16)
          eb79794267854191554e088876646a17
          45daa0af063be1f2e19d22b17c5d51ed
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}