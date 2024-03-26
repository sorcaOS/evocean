import { Injectable } from '@angular/core';
import { AbstractService, User } from '@omelet/shared-components';
import { Wallet } from '../interfaces/wallet';

@Injectable({
  providedIn: 'root'
})
export class UserService extends AbstractService<User> {
  override end_point = '/user';

  public getUserAvatar(user_id: number) {
    return this.get<string>(`${user_id}/avatar`);
  }

  public addWallet(public_key: string) {
    return this.post<Wallet>('/add_wallet', {
      public_key: public_key
    });
  }
}
