import { Component, OnInit, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-wizard',
  templateUrl: './wizard.component.html',
  styleUrls: ['./wizard.component.scss']
})

export class WizardComponent implements OnInit {

  constructor() { }

  public currentSlide = 1;
  public totalSlides = 2;

  @Output() allSlidesShown = new EventEmitter<boolean>();

  ngOnInit(): void {
  }

  public nextSlide() {
    if (this.currentSlide === this.totalSlides) {
      this.allSlidesShown.emit(true);
      return;
    }
    this.currentSlide +=  1;
  }

}
