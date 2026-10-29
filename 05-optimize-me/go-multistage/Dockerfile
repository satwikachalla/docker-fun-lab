# Stage 1: builder (has the compiler)
FROM golang:1.23-alpine AS builder
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /out/server .

# Stage 2: final image (only the result)
FROM alpine:3.20
COPY --from=builder /out/server /app/server
CMD ["/app/server"]
