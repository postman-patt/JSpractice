// The GPS itinerary: Around the World - edabit

// Utility Class
// With utility functions you can call the method straight from the class (e.g. GPS.decimal()) without having to instantiate the object

// Haversine Formular
// a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
// c = 2 ⋅ atan2( √a, √(1−a) )
// d = R ⋅ c

// Note:
// φ = latitude (radians)
// λ = longittude (radians)

class GPS {
  static decimal(degrees, minutes, seconds, directions) {
    return directions == 'S' || directions == 'W'
      ? (degrees + minutes / 60 + seconds / 3600) * -1
      : degrees + minutes / 60 + seconds / 3600
  }

  static radians(decimal) {
    return (decimal * Math.PI) / 180
  }

  static distance(cityA, cityB) {
    //City latitude and longitude (Coordinates --> Decimals --> Radians)

    const cityA_lat = this.radians(
      this.decimal(
        ...cityA
          .replace(/[^A-Za-z0-9 ]/g, '')
          .split(' ')
          .slice(0, 4)
          .map((char) => {
            if (!isNaN(char)) {
              return Number(char)
            } else {
              return char
            }
          })
      )
    )

    const cityA_lon = this.radians(
      this.decimal(
        ...cityA
          .replace(/[^A-Za-z0-9 ]/g, '')
          .split(' ')
          .slice(4)
          .map((char) => {
            if (!isNaN(char)) {
              return Number(char)
            } else {
              return char
            }
          })
      )
    )

    const cityB_lat = this.radians(
      this.decimal(
        ...cityB
          .replace(/[^A-Za-z0-9 ]/g, '')
          .split(' ')
          .slice(0, 4)
          .map((char) => {
            if (!isNaN(char)) {
              return Number(char)
            } else {
              return char
            }
          })
      )
    )
    const cityB_lon = this.radians(
      this.decimal(
        ...cityB
          .replace(/[^A-Za-z0-9 ]/g, '')
          .split(' ')
          .slice(4)
          .map((char) => {
            if (!isNaN(char)) {
              return Number(char)
            } else {
              return char
            }
          })
      )
    )

    const R = 6371e3 // Raidus of Earth (metres)
    const diff_lat = cityB_lat - cityA_lat
    const diff_lon = cityB_lon - cityA_lon

    const a =
      Math.pow(Math.sin(diff_lat / 2), 2) +
      Math.cos(cityB_lat) *
        Math.cos(cityA_lat) *
        Math.pow(Math.sin(diff_lon / 2), 2)

    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))

    return Math.floor((R * c) / 1000) // kilometers
  }
}

// Itinerary Function

const itinerary = (start, toVisit) => {
  let unvisited = [...toVisit]
  let visited = [start]

  let count = 0

  let current = start

  while (visited.length <= toVisit.length) {
    let distancesFromCurrent = unvisited.map((city) => {
      return GPS.distance(cities[current], cities[city])
    })

    let min_index = distancesFromCurrent.indexOf(
      Math.min(...distancesFromCurrent)
    )

    count += Math.min(...distancesFromCurrent)

    current = unvisited[min_index]

    visited.push(...unvisited.splice(min_index, 1))
  }

  return [visited, count]
}

const cities = {
  London: `51° 30' 30" N 0° 7' 32" W`,
  'New York': `40° 42' 51" N 74° 0' 21" W`,
  Kitchener: `43° 27' 10" N 80° 29' 42" W`,
  'Los Angeles': `34° 3' 8" N 118° 14' 37" W`,
  Naples: `40° 51' 46" N 14° 16' 36" E`,
  Moscow: `55° 45' 7" N 37° 36' 56" E`,
  Beijing: `39° 54' 27" N 116° 23' 50" E`,
  Tokyo: `35° 41' 22" N 139° 41' 30" E`,
  Quito: `0° 13' 47" S 78° 31' 29" W`,
  'Buenos Aires': `34° 36' 30" S 58° 22' 19" W`,
  'Rio de Janeiro': `22° 54' 10" S 43° 12' 27" W`,
  Montevideo: `35° 54' 11" S 56° 11' 17" W`,
  Johannesburg: `26° 12' 8" S 28° 2' 37" E`,
  Jakarta: `6° 12' 52" S 106° 50' 42" E`,
  Sidney: `33° 52' 4" S 151° 12' 26" E`,
  Auckland: `36° 52' 0" S 174° 46' 0" E`,
}

console.log(
  itinerary('Naples', ['New York', 'Johannesburg', 'Beijing', 'Quito'])
)
