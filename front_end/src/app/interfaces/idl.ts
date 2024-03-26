export const MY_IDL = {
  'version': '0.1.0',
  'name': 'evocean',
  'instructions': [
    {
      'name': 'hello',
      'accounts': [
        {
          'name': 'signer',
          'isMut': true,
          'isSigner': true
        }
      ],
      'args': []
    },
    {
      'name': 'init',
      'accounts': [
        {
          'name': 'owner',
          'isMut': true,
          'isSigner': true
        },
        {
          'name': 'product',
          'isMut': true,
          'isSigner': false
        },
        {
          'name': 'rent',
          'isMut': false,
          'isSigner': false
        },
        {
          'name': 'systemProgram',
          'isMut': false,
          'isSigner': false
        }
      ],
      'args': [
        {
          'name': 'uid',
          'type': 'string'
        },
        {
          'name': 'price',
          'type': 'u64'
        },
        {
          'name': 'priceOneTime',
          'type': 'u64'
        }
      ]
    }
  ],
  'accounts': [
    {
      'name': 'Product',
      'type': {
        'kind': 'struct',
        'fields': [
          {
            'name': 'owner',
            'type': 'publicKey'
          },
          {
            'name': 'uid',
            'type': 'string'
          },
          {
            'name': 'price',
            'type': 'u64'
          },
          {
            'name': 'priceOneTime',
            'type': 'u64'
          }
        ]
      }
    }
  ]
};