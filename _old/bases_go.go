package main

import (
	"encoding/base64"
	"encoding/hex"
	"fmt"
	"strconv"
	"strings"
)

// Struct for base encoders/decoders
type basesEnD struct{}

func (b basesEnD) EncodeBase1(data string) string {
	return strings.Repeat("1", len(data))
}

func (b basesEnD) DecodeBase1(encoded string) string {
	return strings.Repeat("a", len(encoded))
}

func (b basesEnD) EncodeBase2(data string) string {
	var result strings.Builder
	for _, char := range data {
		result.WriteString(fmt.Sprintf("%08b", char))
	}
	return result.String()
}

func (b basesEnD) DecodeBase2(encoded string) string {
	var result strings.Builder
	for i := 0; i < len(encoded); i += 8 {
		val, _ := strconv.ParseInt(encoded[i:i+8], 2, 64)
		result.WriteByte(byte(val))
	}
	return result.String()
}

func (b basesEnD) EncodeBase4(data string) string {
	var result strings.Builder
	for _, char := range data {
		binary := fmt.Sprintf("%08b", char)
		for _, bit := range binary {
			switch bit {
			case '0':
				result.WriteString("A")
			case '1':
				result.WriteString("B")
			}
		}
	}
	return result.String()
}

func (b basesEnD) DecodeBase4(encoded string) string {
	var result strings.Builder
	for i := 0; i < len(encoded); i += 2 {
		bits := encoded[i : i+2]
		switch bits {
		case "AA":
			result.WriteString("0")
		case "AB":
			result.WriteString("1")
		}
	}
	return b.DecodeBase2(result.String())
}

func (b basesEnD) EncodeBase8(data string) string {
	var result strings.Builder
	for _, char := range data {
		result.WriteString(fmt.Sprintf("%03o", char))
	}
	return result.String()
}

func (b basesEnD) DecodeBase8(encoded string) string {
	var result strings.Builder
	for i := 0; i < len(encoded); i += 3 {
		val, _ := strconv.ParseInt(encoded[i:i+3], 8, 64)
		result.WriteByte(byte(val))
	}
	return result.String()
}

func (b basesEnD) EncodeBase16(data string) string {
	return hex.EncodeToString([]byte(data))
}

func (b basesEnD) DecodeBase16(encoded string) string {
	decoded, _ := hex.DecodeString(encoded)
	return string(decoded)
}

func (b basesEnD) EncodeBase32(data string) string {
	return base64.StdEncoding.EncodeToString([]byte(data))
}

func (b basesEnD) DecodeBase32(encoded string) string {
	decoded, _ := base64.StdEncoding.DecodeString(encoded)
	return string(decoded)
}

func (b basesEnD) EncodeBase64(data string) string {
	return base64.StdEncoding.EncodeToString([]byte(data))
}

func (b basesEnD) DecodeBase64(encoded string) string {
	decoded, _ := base64.StdEncoding.DecodeString(encoded)
	return string(decoded)
}

func (b basesEnD) EncodeBase128(data string) string {
	return base64.StdEncoding.EncodeToString([]byte(data))
}

func (b basesEnD) DecodeBase128(encoded string) string {
	decoded, _ := base64.StdEncoding.DecodeString(encoded)
	return string(decoded)
}

func (b basesEnD) EncodeBase256(data string) []byte {
	return []byte(data)
}

func (b basesEnD) DecodeBase256(encoded []byte) string {
	return string(encoded)
}

func main() {
	encoder := basesEnD{}
	data := "Hello, World!"

	encoded := encoder.EncodeBase64(data)
	fmt.Println("Encoded Base64:", encoded)

	decoded := encoder.DecodeBase64(encoded)
	fmt.Println("Decoded Base64:", decoded)
}
