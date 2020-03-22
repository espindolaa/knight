import { Component, OnInit, Input } from '@angular/core';
import { AlgebraicPosition } from 'src/model/algebraic-position';

@Component({
  selector: 'app-chess-cell',
  templateUrl: './chess-cell.component.html',
  styleUrls: ['./chess-cell.component.scss']
})
export class ChessCellComponent implements OnInit {

  @Input() public position: AlgebraicPosition;

  constructor() {
   }

  ngOnInit(): void {
  }

}
