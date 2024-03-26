import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class Web3Service {
  private provider: any;

  constructor(private http: HttpClient) {
    this.provider = this.getProvider();
  }

  private getProvider() {
    if ('phantom' in window) {
      let provider: any;
      // @ts-ignore
      provider = window.phantom['solana'];

      if (provider) {
        return provider;
      }
    }
    return null;
  }

  public async connectWeb3Wallet() {
    if (!this.provider) {
      return;
    }

    try {
      await this.provider.connect();
      const publicKey = await this.provider.publicKey;
      return publicKey;
    } catch (e) {
      console.error(e);
    }
  }

  public getSolPrice() {
    const url = 'https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd';

    return this.http.get(url);
  }

}