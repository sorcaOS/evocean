from seahorse.prelude import *

declare_id('59mLTDkzoXWmpGFc6xRehWsWJnmpzaQ4xndiUWzruM1k')


class Product(Account):
    owner: Pubkey
    author: Pubkey
    uid: str
    price: u64
    price_one_time: u64
    allow_bid: bool
    owner_token_account: Pubkey
    author_token_account: Pubkey


class Profile(Account):
    owner: Pubkey
    token_account: Pubkey
    is_faucet_profile: u16


class Offer(Account):
    owner: Pubkey
    product: Pubkey
    offer_price: u64
    offer_method: str
    product_owner: Pubkey
    status: str


class Order(Account):
    owner: Pubkey
    product: Pubkey
    product_owner: Pubkey
    status: str


@instruction
def create_product(signer: Signer, product: Empty[Product], uid: str, price: u64,
                   price_one_time: u64,
                   allow_bid: bool,
                   ownerTokenAccount: TokenAccount,
                   author_token_account: TokenAccount,
                   authorProfile: Profile,
                   ownerProfile: Profile):
    assert signer.key() == ownerProfile.owner, 'Need to create profile first'
    assert ownerTokenAccount.key() == ownerProfile.token_account, 'False validate owner token account'
    assert author_token_account.key() == authorProfile.token_account, 'False validate author token account'

    product = product.init(payer=signer, seeds=['create_product', signer, uid])
    product.owner = signer.key()
    product.author = signer.key()
    product.uid = uid
    product.price = price
    product.price_one_time = price_one_time
    product.allow_bid = allow_bid

    product.owner_token_account = ownerTokenAccount.key()
    product.author_token_account = author_token_account.key()


@instruction
def create_offer(signer: Signer,
                 offer: Empty[Offer],
                 product: Product,
                 offer_price: u64,
                 offer_method: str,
                 signer_token_account: TokenAccount,
                 product_owner_token_account: TokenAccount,
                 signer_profile: Profile,
                 product_owner_profile: Profile,

                 faucet_token_account: TokenAccount,
                 faucet_profile: Profile
                 ):
    assert signer_profile.token_account == signer_token_account.key(), 'Need to link token account to profile'
    assert signer.key() == signer_profile.owner, 'Need to link token account to profile'
    assert product_owner_profile.token_account == product_owner_token_account.key(), 'Need to link token account to profile'
    assert product_owner_profile.owner == product.owner, 'Validate owner profile'
    assert faucet_profile.token_account == faucet_token_account.key(), 'Need to link token account to profile'
    assert faucet_profile.is_faucet_profile==1, 'Need to link token faucet profile'

    offer = offer.init(payer=signer, seeds=['create_offer', signer, product.key(), product.owner])
    offer.owner = signer.key()
    offer.product_owner = product.owner
    offer.product = product.key()
    offer.offer_price = offer_price
    offer.offer_method = offer_method

    signer.transfer_lamports(faucet_token_account, offer_price)

    offer.status = 'deposited'


@instruction
def create_oder(signer: Signer, order: Empty[Order],
                product: Product,
                signer_token_account: TokenAccount,
                signer_profile: Profile,
                product_owner_token_account: TokenAccount):
    assert product_owner_token_account.key() == product.owner_token_account, 'Need transfer token to product owner'
    assert signer_profile.token_account == signer_token_account.key(), 'Need to link token account to profile'

    order = order.init(payer=signer, seeds=['create_oder', signer, product.uid])
    order.owner = signer.key()
    order.product_owner = product.owner
    order.product = product.key()
    signer.transfer_lamports(product_owner_token_account, product.price)
    order.status = 'paid'


@instruction
def confirm_offer(signer: Signer, offer: Offer,
                  product_owner_token_account: TokenAccount,
                  product_owner_profile: Profile,
                  faucet_token_account: TokenAccount,
                  faucet_profile: Profile
                  ):
    # only the product owner can confirm the offer
    assert signer.key() == offer.product_owner, 'Only the product owner can confirm the offer'
    assert product_owner_token_account.key() == offer.product_owner, 'Need transfer token to product owner'
    assert product_owner_profile.token_account == product_owner_token_account.key(), 'Need to link token account to profile'
    assert faucet_profile.token_account == faucet_token_account.key(), 'Need to link token account to profile'
    assert faucet_profile.is_faucet_profile==1, 'Need to link token faucet profile'

    faucet_profile.transfer_lamports(product_owner_token_account, offer.offer_price)
    offer.status = 'confirmed'


@instruction
def cancel_offer(signer: Signer,
                 offer: Offer,
                 signer_token_account: TokenAccount,
                 faucet_token_account: TokenAccount,
                 faucet_profile: Profile

                 ):
    # only the offer owner can cancel the offer
    assert signer.key() == offer.owner, 'Only the offer owner can cancel the offer'
    assert faucet_profile.token_account == faucet_token_account.key(), 'Need to link token account to profile'
    assert faucet_profile.is_faucet_profile==1, 'Need to link token faucet profile'

    faucet_profile.transfer_lamports(signer_token_account, offer.offer_price)
    offer.status = 'cancelled'


@instruction
def create_profile(signer: Signer, account: Empty[Profile], token_account: TokenAccount, is_faucet_profile: u16):

    account = account.init(payer=signer, seeds=['create_account', signer, is_faucet_profile])
    account.owner = signer.key()
    account.token_account = token_account.key()
    account.is_faucet_profile = is_faucet_profile
