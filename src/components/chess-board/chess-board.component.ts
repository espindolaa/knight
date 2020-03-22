import { Component, OnInit } from '@angular/core';
import { AlgebraicPosition } from 'src/model/algebraic-position';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-chess-board',
  templateUrl: './chess-board.component.html',
  styleUrls: ['./chess-board.component.scss']
})
export class ChessBoardComponent implements OnInit {

  public cellsPosition: AlgebraicPosition[] = [];

  public knightPosition$ = new BehaviorSubject<AlgebraicPosition>(null);
  public highlightedPositions$ = new BehaviorSubject<AlgebraicPosition[]>([]);

  ngOnInit(): void {
    this._generateCells();
  }

  private _generateCells() {
    const columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
    const rows = [8, 7, 6, 5, 4, 3, 2, 1];

    rows.forEach(row => {
      columns.forEach(column => this.cellsPosition.push(new AlgebraicPosition(column, row)));
    });
  }
    
  public updateChosenCell(position) {
    this.knightPosition$.next(position);
    this.highlightedPositions$.next(this.cellsPosition);
  }
}
