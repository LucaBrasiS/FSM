`timescale 1ns / 1ps

module Lock_Door (
    input  logic        clk,
    input  logic        rst,
    input  logic        in,
    output logic        unlocked,
    output logic [1:0]  screen
);

    // Durumlar (States) için modern enum tanımı
    typedef enum logic [3:0] {
        S_IDLE = 4'b0001,
        S_1    = 4'b0010,
        S_2    = 4'b0100,
        S_3    = 4'b1000
    } state_t;

    state_t cs, ns;

    // Ekran Durum Mesajları
    localparam logic [1:0] SIFRE_GIRINIZ      = 2'b00;
    localparam logic [1:0] ILK_HANE_HATALI    = 2'b01;
    localparam logic [1:0] IKINCI_HANE_HATALI = 2'b10;
    localparam logic [1:0] HOSGELDINIZ        = 2'b11;

    // Sistemin kabul edeceği gizli şifre (Örneğin: 3 bitlik "101" şifresi)
    localparam logic [2:0] TARGET_PASSWORD = 3'b101;

    logic [2:0] in_password;
    logic [1:0] syc_in; // 0, 1, 2 basamak sayacı

    // 1. Adım: Durum Hafızası (Sequential Logic)
    always_ff @(posedge clk or posedge rst) begin
        if (rst) 
            cs <= S_IDLE;
        else     
            cs <= ns;
    end

    // 2. Adım: Tuş Basma ve Sayaç Yönetimi
    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            in_password <= 3'b000;
            syc_in      <= 2'd0;
            screen      <= SIFRE_GIRINIZ;
            unlocked    <= 1'b0;
        end else begin
            // Dışarıdan gelen seri bitleri sırayla diziye kaydet
            in_password[syc_in] <= in;

            // Sayaç yönetimi (0 -> 1 -> 2 -> 0)
            if (syc_in == 2'd2) 
                syc_in <= 2'd0;
            else 
                syc_in <= syc_in + 1'b1;

            // Ekranda gösterilecek uyarıları duruma göre ayarla
            case (cs)
                S_IDLE: begin
                    screen   <= SIFRE_GIRINIZ;
                    unlocked <= 1'b0;
                end
                S_1: begin
                    if (in_password[0] != TARGET_PASSWORD[0])
                        screen <= ILK_HANE_HATALI;
                    else
                        screen <= SIFRE_GIRINIZ;
                end
                S_2: begin
                    if (in_password[1] != TARGET_PASSWORD[1])
                        screen <= IKINCI_HANE_HATALI;
                end
                S_3: begin
                    screen   <= HOSGELDINIZ;
                    unlocked <= 1'b1;
                end
                default: begin
                    screen   <= SIFRE_GIRINIZ;
                    unlocked <= 1'b0;
                end
            endcase
        end
    end

    // 3. Adım: Sonraki Durum Mantığı (Combinational Logic)
    always_comb begin
        ns = cs; // Varsayılan olarak aynı durumda kal
        case (cs)
            S_IDLE: begin
                if (syc_in == 2'd1) begin
                    if (in_password[0] == TARGET_PASSWORD[0]) ns = S_1;
                    else                                      ns = S_IDLE;
                end
            end

            S_1: begin
                if (syc_in == 2'd2) begin
                    if (in_password[1] == TARGET_PASSWORD[1]) ns = S_2;
                    else                                      ns = S_IDLE;
                end
            end

            S_2: begin
                if (syc_in == 2'd0) begin
                    if (in_password[2] == TARGET_PASSWORD[2]) ns = S_3;
                    else                                      ns = S_IDLE;
                end
            end

            S_3: begin
                ns = S_IDLE; // Kapı açıldıktan sonra başa dön
            end

            default: ns = S_IDLE;
        endcase
    end

endmodule