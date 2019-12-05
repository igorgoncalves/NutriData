import Indicador from "./indicador";

export default class Macroindicador {
  constructor({ id, nome, descricao, indicadores }) {
    this.id = id;
    this.nome = nome;
    this.descricao = descricao;
    this.indicadores = indicadores.map(
      (indicador) => new Indicador({ ...indicador })
    );
  }
}
