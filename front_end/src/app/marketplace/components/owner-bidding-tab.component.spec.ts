import { ComponentFixture, TestBed } from '@angular/core/testing';
import { OwnerBiddingTabComponent } from './owner-bidding-tab.component';

describe('ReviewTabComponent', () => {
  let component: OwnerBiddingTabComponent;
  let fixture: ComponentFixture<OwnerBiddingTabComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OwnerBiddingTabComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(OwnerBiddingTabComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
