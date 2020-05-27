import Indicador from "./indicador";

export default class Macroindicador {
  constructor({ id, nome, categoria, descricao, indicadores }) {
    this.id = id;
    this.nome = nome;
    this.descricao = descricao;
    this.categoria = categoria;
    this.indicadores = indicadores.map(
      (indicador) => new Indicador({ ...indicador })
    );
  }
}
