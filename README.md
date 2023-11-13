# Lane

## Objectif du projet

Cartographier et classer les obstructions dans la piste cyclable à signaler à la
ville de Montréal.

## Fonctionnement

Vous pouvez afficher index.geojson dans un outil de visualisation de carte tel que [kepler.gl](https://kepler.gl/)
ou [directement dans Github](https://github.com/rngadam/lane-data/blob/main/index.geojson)

## Génération des données à partir des images sources

```bash
sudo apt update
sudo apt install -y exiftool
./exif-extract.sh
./convert_to_geojson.py
```


## Origine du nom du projet

En l'honneur de Albert T. Lane, le premier cycliste en Amérique du Nord:

> On July 1, 1874, Albert T. Lane, a bookkeeper residing at 16 Fournier Street in
> Montreal, rode the first bicycle ever seen in North America through the streets
> of Montreal. It was a penny-farthing style of bicycle, also known as a high
> wheel or high wheeler, with a 50-inch diameter front wheel and a much smaller
> rear wheel, and it represented a revolution in transportation. Wealthier
> citizens began to buy bicycles from Britain and France and in 1878, under Lane’s
> initiative, the Montreal Bicycle Club (MBC) was founded. Shortly after, the MBC
> merged with the Montreal Lacrosse Club and the Montreal Snow Shoe Club to form
> the Montreal Amateur Athletic Association or MAAA.

https://www.westmountmag.ca/cycling/

## TODO

* les positions GPS rapportés ne semblent pas correspondre assez précisément à
  la vrai position de capture

  * c'est possible qu'en accédant l'application photo du téléphone mobile la
    position n'est pas à jour ou imprécise
  * éliminer les points redondants qui ne sont pas près d'une vraie piste cyclable